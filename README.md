# take_screenshot_loop

This code defines a simple Python application using the Tkinter library to create a GUI for taking screenshots at regular intervals. The application allows the user to specify parameters such as the object file name, monitor dimensions, display time between screenshots, initial image index, and the directory where the screenshots will be saved. It continuously captures screenshots until the user stops the process.

Here's a step-by-step guide on how to use the provided code:

##Tutorial: Creating a Screenshot Looper with Tkinter

###Step 1: Install Required Libraries

Make sure you have Python installed on your system. Additionally, install the required libraries using the following command:

```bash
pip install pillow tkinter
```

###Step 2: Save the Code

Copy the provided code and save it in a file, for example, screenshot_looper.py.

###Step 3: Run the Application

Open a terminal, navigate to the directory containing the saved script, and run the following command:

```bash
python screenshot_looper.py
```

###Step 4: Configure Settings:

Enter the desired values in the Entry widgets:
Object File Name: The prefix for the screenshot filenames.
Monitor (left, top, right, bottom): Define the area on the screen to capture in the format left, top, right, bottom.
Display Time (seconds): Set the time interval between each screenshot.
Initial Image Index: The starting index for the screenshot filenames.
Directory: The directory where screenshots will be saved.

###Step 5: Start and Stop Capture:

Click the "Start" button to begin capturing screenshots with the specified settings.
Click the "Stop" button to stop the screenshot capture process.

###Step 6: Review Captured Screenshots

Navigate to the specified directory to find the captured screenshots. The filenames will be in the format {object_file_name}_{image_index}.jpg.

##Notes:

If the specified directory does not exist, the application will create it.
If an error occurs during the capture process, an error message will be displayed.

##Conclusion

This simple Tkinter application provides a convenient way to capture screenshots at regular intervals, making it useful for tasks like creating datasets or monitoring visual changes over time. Customize the settings based on your specific requirements, and enjoy the ease of capturing screenshots with this user-friendly interface.
