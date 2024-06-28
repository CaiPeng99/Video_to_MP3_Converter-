import pika, json


def upload(f, fs, channel, access):
    #  try:
    #         # if f:
    #         fid = fs.put(f)
    #     except Exception as err:
    #         return f"Error putting file into file system:{err}", 500

    try:
       fid = fs.put(f)
    except Exception as err:
        # print(f"Error putting file into file system: {err}")
        # return "First internal server error", 500
        # return f"f is :{f}, fs is :{fs}, channel is :{channel}, access is {access}", 500
        return f"Error putting file into file system:{err}", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        # print(f"Final Error : {err}")
        return f"Last Error putting file into file system:{err}", 500
        fs.delete(fid)
        
        # return "Last internal server error"