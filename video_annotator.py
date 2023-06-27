import cv2
import csv

def create_word_overlay(frame, word):
    # Add the word overlay to the frame
    if(word == 'HIT'):
        cv2.putText(frame, word, (1000, 600), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)
    else:
        cv2.putText(frame, word, (100,  100), cv2.FONT_HERSHEY_TRIPLEX, 1, (50, 50, 255), 2)

    return frame

def process_video_with_csv(video_file, csv_file, output_file):
    # Read the video file
    video_capture = cv2.VideoCapture(video_file)
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Adjust the codec as per your requirement
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    # Open the CSV file
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        hit_counter = persistence_frames
        bounce_counter = persistence_frames
        i = 0
        # Iterate through each row in the CSV file
        for row in csv_reader:
            i+=1
            if i == 1 or i == 2:
                continue
            # Extract the frame image from the video
            ret, frame = video_capture.read()

            # Check if the frame contains a 1
            if int(row[-1]) == 1:
                # Add the word overlay to the frame
                bounce_counter = persistence_frames
                frame = create_word_overlay(frame, 'BOUNCE')

            elif int(row[-1]) == 2:
            # Add the word overlay to the frame
                hit_counter = persistence_frames
                frame = create_word_overlay(frame, 'HIT')
            else:
                if hit_counter > 0:
                    frame = create_word_overlay(frame, 'HIT')
                    hit_counter -= 1
                if bounce_counter > 0:
                    frame = create_word_overlay(frame, 'BOUNCE')
                    bounce_counter -=1
                    
            # Write the frame to the output video file
            video_writer.write(frame)

            # Display the resulting frame (for testing purposes)
            #cv2.imshow('Video with Word Overlay', frame)
            #if cv2.waitKey(25) & 0xFF == ord('q'):
                #break

    # Release the video capture, video writer, and close the window
    video_capture.release()
    video_writer.release()
    cv2.destroyAllWindows()

# Provide the video file and CSV file paths as inputs
video_file = './final_scripts/tennis_8.mp4'
csv_file = './new_dataset/tennis_8_final.csv'
output_file = './final_scripts/output.mp4'
persistence_frames = 5

# Process the video with the CSV file and save the output
process_video_with_csv(video_file, csv_file, output_file)
