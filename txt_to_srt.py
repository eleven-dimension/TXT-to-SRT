def txt_to_srt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as f:
        subtitle_index = 1
        for index, line in enumerate(lines):
            if not line.strip():
                continue

            start_seconds = (subtitle_index - 1) * 10
            end_seconds = start_seconds + 10
            
            start_time = convert_seconds_to_timestamp(start_seconds)
            end_time = convert_seconds_to_timestamp(end_seconds)
            
            f.write(f"{subtitle_index}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{line.strip()}\n\n")

            subtitle_index += 1


def convert_seconds_to_timestamp(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    milliseconds = 0
    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"


if __name__ == "__main__":
    input_txt_file = "input.txt"
    output_srt_file = "output.srt"
    
    txt_to_srt(input_txt_file, output_srt_file)
