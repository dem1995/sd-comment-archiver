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
        video_ids = json.load(video_ids)
        video_ids_considered = video_ids[args.start:args.finish]
    
    with open(f"archival_script_{args.start}_through_{ending_note}.sh", 'w') as archival_script:
        archival_script.write("#!/bin/bash\n")
        for offset_index, vid_id in enumerate(video_ids[args.start:args.finish]):
            id_index = offset_index + args.start
            vid_index = "????"  #Until we get the YT ids ordered
            archival_script.write(f"python downloader.py --youtubeid=\"{vid_id}\" --output SD_Best_VGM_{vid_index}_id_index_{id_index}_with_vid_id_{vid_id}.json\n")