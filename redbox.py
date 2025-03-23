from depthai_sdk import OakCamera
import depthai

with OakCamera(usb_speed=depthai.UsbSpeed.HIGH) as oak: #Oakd Camera was connected to the jetson with a USB cord
    color = oak.create_camera('color')
    model_config = {
        'source': 'roboflow', # Specify that we are downloading the model from Roboflow
        'model':'red-box-detection-mae125/2', # Model name to identify the reb box (object to pick up)
        'key':'123456' # Replace with your own API key
        }
    nn = oak.create_nn(model_config, color)
    oak.visualize(nn, fps=True)
    oak.start(blocking=True)
