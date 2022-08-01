{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35e91ea4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Using TensorFlow backend.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [01/Aug/2022 22:55:21] \"GET / HTTP/1.1\" 200 -\n",
      "[2022-08-01 22:56:20,616] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 2073, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1519, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1517, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1503, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)\n",
      "  File \"C:\\Users\\14416\\AppData\\Local\\Temp\\ipykernel_13216\\364418272.py\", line 18, in upload_file\n",
      "    model = load_model(\"Pneumonia\")\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\", line 492, in load_wrapper\n",
      "    return load_function(*args, **kwargs)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\", line 583, in load_model\n",
      "    with H5Dict(filepath, mode='r') as h5dict:\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\utils\\io_utils.py\", line 191, in __init__\n",
      "    self.data = h5py.File(path, mode=mode)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\", line 507, in __init__\n",
      "    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\", line 220, in make_fid\n",
      "    fid = h5f.open(name, flags, fapl=fapl)\n",
      "  File \"h5py\\_objects.pyx\", line 54, in h5py._objects.with_phil.wrapper\n",
      "  File \"h5py\\_objects.pyx\", line 55, in h5py._objects.with_phil.wrapper\n",
      "  File \"h5py\\h5f.pyx\", line 106, in h5py.h5f.open\n",
      "PermissionError: [Errno 13] Unable to open file (unable to open file: name = 'Pneumonia', errno = 13, error message = 'Permission denied', flags = 0, o_flags = 0)\n",
      "127.0.0.1 - - [01/Aug/2022 22:56:20] \"POST / HTTP/1.1\" 500 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File Received\n",
      "person1949_bacteria_4880.jpeg\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[2022-08-01 22:56:26,247] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 2073, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1519, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1517, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1503, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)\n",
      "  File \"C:\\Users\\14416\\AppData\\Local\\Temp\\ipykernel_13216\\364418272.py\", line 18, in upload_file\n",
      "    model = load_model(\"Pneumonia\")\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\", line 492, in load_wrapper\n",
      "    return load_function(*args, **kwargs)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\", line 583, in load_model\n",
      "    with H5Dict(filepath, mode='r') as h5dict:\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\utils\\io_utils.py\", line 191, in __init__\n",
      "    self.data = h5py.File(path, mode=mode)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\", line 507, in __init__\n",
      "    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\", line 220, in make_fid\n",
      "    fid = h5f.open(name, flags, fapl=fapl)\n",
      "  File \"h5py\\_objects.pyx\", line 54, in h5py._objects.with_phil.wrapper\n",
      "  File \"h5py\\_objects.pyx\", line 55, in h5py._objects.with_phil.wrapper\n",
      "  File \"h5py\\h5f.pyx\", line 106, in h5py.h5f.open\n",
      "PermissionError: [Errno 13] Unable to open file (unable to open file: name = 'Pneumonia', errno = 13, error message = 'Permission denied', flags = 0, o_flags = 0)\n",
      "127.0.0.1 - - [01/Aug/2022 22:56:26] \"POST / HTTP/1.1\" 500 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File Received\n",
      "person1949_bacteria_4880.jpeg\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[2022-08-01 22:56:28,256] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 2073, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1519, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1517, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1503, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)\n",
      "  File \"C:\\Users\\14416\\AppData\\Local\\Temp\\ipykernel_13216\\364418272.py\", line 18, in upload_file\n",
      "    model = load_model(\"Pneumonia\")\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\", line 492, in load_wrapper\n",
      "    return load_function(*args, **kwargs)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\", line 583, in load_model\n",
      "    with H5Dict(filepath, mode='r') as h5dict:\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\utils\\io_utils.py\", line 191, in __init__\n",
      "    self.data = h5py.File(path, mode=mode)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\", line 507, in __init__\n",
      "    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\", line 220, in make_fid\n",
      "    fid = h5f.open(name, flags, fapl=fapl)\n",
      "  File \"h5py\\_objects.pyx\", line 54, in h5py._objects.with_phil.wrapper\n",
      "  File \"h5py\\_objects.pyx\", line 55, in h5py._objects.with_phil.wrapper\n",
      "  File \"h5py\\h5f.pyx\", line 106, in h5py.h5f.open\n",
      "PermissionError: [Errno 13] Unable to open file (unable to open file: name = 'Pneumonia', errno = 13, error message = 'Permission denied', flags = 0, o_flags = 0)\n",
      "127.0.0.1 - - [01/Aug/2022 22:56:28] \"POST / HTTP/1.1\" 500 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File Received\n",
      "person1949_bacteria_4880.jpeg\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [01/Aug/2022 22:56:33] \"GET / HTTP/1.1\" 200 -\n",
      "[2022-08-01 22:56:38,252] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 2073, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1519, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1517, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1503, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)\n",
      "  File \"C:\\Users\\14416\\AppData\\Local\\Temp\\ipykernel_13216\\364418272.py\", line 18, in upload_file\n",
      "    model = load_model(\"Pneumonia\")\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\", line 492, in load_wrapper\n",
      "    return load_function(*args, **kwargs)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\engine\\saving.py\", line 583, in load_model\n",
      "    with H5Dict(filepath, mode='r') as h5dict:\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\keras\\utils\\io_utils.py\", line 191, in __init__\n",
      "    self.data = h5py.File(path, mode=mode)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\", line 507, in __init__\n",
      "    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)\n",
      "  File \"C:\\Users\\14416\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\h5py\\_hl\\files.py\", line 220, in make_fid\n",
      "    fid = h5f.open(name, flags, fapl=fapl)\n",
      "  File \"h5py\\_objects.pyx\", line 54, in h5py._objects.with_phil.wrapper\n",
      "  File \"h5py\\_objects.pyx\", line 55, in h5py._objects.with_phil.wrapper\n",
      "  File \"h5py\\h5f.pyx\", line 106, in h5py.h5f.open\n",
      "PermissionError: [Errno 13] Unable to open file (unable to open file: name = 'Pneumonia', errno = 13, error message = 'Permission denied', flags = 0, o_flags = 0)\n",
      "127.0.0.1 - - [01/Aug/2022 22:56:38] \"POST / HTTP/1.1\" 500 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File Received\n",
      "person1949_bacteria_4880.jpeg\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "from werkzeug.utils import secure_filename\n",
    "from skimage import io\n",
    "from keras.models import load_model\n",
    "import cv2 #remove for cloud\n",
    "from PIL import Image #use PIL\n",
    "import numpy as np\n",
    "app = Flask(__name__)\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def upload_file():\n",
    "    if request.method == 'POST':\n",
    "        file = request.files['file']\n",
    "        print(\"File Received\")\n",
    "        filename = secure_filename(file.filename)\n",
    "        print(filename)\n",
    "        file.save(\"./static/\"+filename) #remove when cloud\n",
    "        file = open(\"./static/\"+filename,\"r\") #remove when cloud\n",
    "        model = load_model(\"Pneumonia\")\n",
    "        image = cv2.imread(\"./static/\"+filename) #remove for cloud\n",
    "        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #remove for cloud\n",
    "        img = cv2.merge([gray,gray,gray]) #remove for cloud\n",
    "# for cloud add this (cloud need to use PIL instead of CV2): image = Image.open(file)\n",
    "# for cloud add this: img = np.asarray(image)\n",
    "        img.resize((150,150,3))\n",
    "        img = np.asarray(img, dtype=\"float32\") #need to transfer to np to reshape\n",
    "        img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2]) #rgb to reshape to 1,100,100,3\n",
    "        pred=model.predict(img)\n",
    "        return(render_template(\"index.html\", result=str(pred)))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result=\"WAITING\"))\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25a2107b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "tensorflow",
   "language": "python",
   "name": "tensorflow"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
