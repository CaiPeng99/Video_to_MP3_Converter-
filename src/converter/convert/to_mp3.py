import pika, json, tempfile, os
from bson.objectid import ObjectId
import moviepy.editor

def start(message, fs_video, fs_mp3s, channel):
   # deserialize a str instance
   # contain a JSON document to a py obj
   message = json.loads(message)
   
   # empty temp file
   tf = tempfile.NamedTemporaryFile()
   # video contents
   # using "video_fid" to find str accordingly, and get the object based on it, use object version of it to get from MongoDB
   out = fs_video.get(ObjectId(message["video_fid"]))
   # add video contents to empty file
   tf.write(out.read())
   # create audio from temp video file
   audio = moviepy.editor.VideoFileClip(tf.name).audio
   tf.close()

   # write audio to the file
   tf_path = tempfile.gettempdir() + f"/{message['video_fid']}.mp3"
   audio.write_audiofile(tf_path)
   
   # save file to mongo
   f = open(tf_path, "rb")
   data = f.read()
   fid = fs_mp3s.put(data)
   f.close()
   os.remove(tf_path)
   
   message["mp3_fid"] = str(fid)
   try:
        channel.basic_publish(
            exchange="",
            routing_key=os.environ.get("MP3_QUEUE"),
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
   except Exception as err:
        fs_mp3s.delete(fid)
        return "failed to publish message"   
