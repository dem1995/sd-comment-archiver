import json
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A program that prepares a bash script for downloading comments from a range of SupraDarky's videos.")
    parser.add_argument('-s', '--start', type=int, default=1,
        help="The id (possibly also video) number to start archival at (inclusive). Defaults to 1.")
    parser.add_argument('-f', '--finish', type=int, default=None,
        help="The id (possibly also video) number to end at (exclusive). Defaults to None (goes through last video).")
    args = parser.parse_args()

    if args.finish is not None:
        ending_note = args.finish-1
    else:
        ending_note = "the_end"
    print(f"Collecting comments from video {args.start} up through (including) {ending_note}.")

    with open('video-ids.txt', ) as video_ids:
        video_ids = video_ids.readlines()
        video_ids_considered = video_ids[args.start:args.finish]
    
    with open(f"archival_script_{args.start}_through_{ending_note}.sh", 'w') as archival_script:
        archival_script.write("#!/bin/bash\n")
        for offset_index, vid_string in enumerate(video_ids[args.start:args.finish]):
            yt_id = vid_string[0:11]
            title = vid_string[14:-1]
            #print(f"ID:{yt_id}, Title:{title}")
            id_index = offset_index + args.start
            #vid_index = "????"  #Until we get the YT ids ordered
            archival_script.write(f'echo "Archiving SD video {id_index}, {title}\'s comments (YouTube id {yt_id}...)"\n')
            archival_script.write(f"python downloader.py --youtubeid=\"{yt_id}\" --output=\"SD{id_index:04d} {title}'s comments (YT ID {yt_id}).json\"\n")