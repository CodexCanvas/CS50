""" prompt the user for a file extesion and output the file's media type """

def main():
    set_color(34)  # Set color to blue
    print()
    print("-Enter a file extension to get its media type.")
    print("-type EXIT to end the program")
    reset_color()
    while True:
        ext = input("File.extension:> ").strip().lower()
        if ext == "exit":
            print("Goodbye!")
            break

        match ext:
            case ext if ext.endswith(".gif"):
                print("image/gif")
            case ext if ext.endswith(".jpg") | ext.endswith(".jpeg"):
                print("image/jpeg")
            case ext if ext.endswith(".png"):
                print("image/png")
            case ext if ext.endswith(".pdf"):
                print("application/pdf")
            case ext if ext.endswith(".txt"):
                print("text/plain")
            case ext if ext.endswith(".zip"):
                print("application/zip")
            case ext if ext.endswith(".mp3"):
                print("audio/mpeg")
            case ext if ext.endswith(".mp4"):
                print("video/mp4")
            case _:
                print("application/octet-stream")


def set_color(color_code):
    print(f"\033[{color_code}m", end="")
def reset_color():
    print("\033[0m", end="")

main()