def bye():

    import cv2

    # Open the video file
    # Replace 'your_video.mp4' with your video file's path
    cap = cv2.VideoCapture('animations/bye.mp4')

    if not cap.isOpened():
        print("Error: Could not open video.")
    else:
        # Loop through the frames
        while cap.isOpened():
            # Read a frame
            ret, frame = cap.read()

            if ret:
                # Display the frame in a window named 'Video'
                cv2.imshow('Video', frame)

                # Wait for a key press (1ms delay) and break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                # Break the loop if no more frames are read (end of video)
                break

        # Release the video capture object and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

def idle_animation():
    import cv2

    def play_video_loop(video_path):
        """
        Plays a video file in an infinite loop.

        Args:
            video_path (str): The file path to the video.
        """
        print(f"Attempting to play video: {video_path}")
        
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Could not open video {video_path}")
            return

        while True:
            # Read a frame
            ret, frame = cap.read()

            # Check if frame was read successfully
            if not ret:
                # If the video has ended (ret is False), reset video position
                print("Video ended, restarting...")
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
                
            # Display the frame
            cv2.imshow('Video Loop', frame)

            # Check for key press to exit (press 'q')
            # waitKey(25) means the frame is displayed for 25ms
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video capture object and close all windows
        cap.release()
        cv2.destroyAllWindows()

    # Replace 'your_video.mp4' with the path to your video file
    video_file = 'animations/idle.mp4' 
    play_video_loop(video_file)


def speaking_animation():
    import cv2

    def play_video_loop(video_path):
        """
        Plays a video file in an infinite loop.

        Args:
            video_path (str): The file path to the video.
        """
        print(f"Attempting to play video: {video_path}")
        
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Could not open video {video_path}")
            return

        while True:
            # Read a frame
            ret, frame = cap.read()

            # Check if frame was read successfully
            if not ret:
                # If the video has ended (ret is False), reset video position
                print("Video ended, restarting...")
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
                
            # Display the frame
            cv2.imshow('Video Loop', frame)

            # Check for key press to exit (press 'q')
            # waitKey(25) means the frame is displayed for 25ms
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video capture object and close all windows
        cap.release()
        cv2.destroyAllWindows()

    # Replace 'your_video.mp4' with the path to your video file
    video_file = 'animations/talking.mp4' 
    play_video_loop(video_file)
