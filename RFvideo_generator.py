import cv2
import csv
import sys

def create_word_overlay(frame, word):
    if(word == 'HIT'):
        cv2.putText(frame, word, (1000, 600), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)
    else:
        cv2.putText(frame, word, (100,  100), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)

    return frame

def process_video_with_csv(video_file, csv_file, output_file):
    video_capture = cv2.VideoCapture(video_file)
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        i = 0
        for row in csv_reader:
            i+=1
            if i == 1 or i == 2:
                continue
            ret, frame = video_capture.read()

            if int(row[-1]) == 1:
                frame = create_word_overlay(frame, 'BOUNCE')

            elif int(row[-1]) == 2:
                frame = create_word_overlay(frame, 'HIT')

                    
            video_writer.write(frame)


    video_capture.release()
    video_writer.release()
    cv2.destroyAllWindows()


if(len(sys.argv) < 3):
    print('run as: "python3 RFvideo_generator.py <video> <csv_file> <output_file>"')
    exit(1)

video_file = sys.argv[1]
csv_file = sys.argv[2]
output_file = sys.argv[3]

process_video_with_csv(video_file, csv_file, output_file)
