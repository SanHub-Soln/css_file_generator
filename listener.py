# import time
# import os
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
#
#
# class FileModificationHandler(FileSystemEventHandler):
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.previous_content = ""
#
#     def on_modified(self, event):
#         # Only monitor the specified file for changes
#         if event.src_path == self.file_path:
#             with open(self.file_path, 'r') as file:
#                 current_content = file.read()
#
#             # Compare current content with previous content
#             if current_content != self.previous_content:
#                 self.detect_last_modified_line(self.previous_content, current_content)
#                 self.previous_content = current_content
#
#     def detect_last_modified_line(self, previous_content, current_content):
#         # Split content into lines
#         previous_lines = previous_content.splitlines()
#         current_lines = current_content.splitlines()
#
#         # Find the last modified line
#         if len(current_lines) > len(previous_lines):
#             # New line added
#             last_modified_line = current_lines[-1]
#             line_number = len(current_lines)  # Line number is the index + 1
#             print(f"New line added: {last_modified_line} (Line {line_number})")
#         else:
#             # Compare lines to find the last modified
#             for idx, (old, new) in enumerate(zip(previous_lines, current_lines)):
#                 if old != new:
#                     last_modified_line = new
#                     line_number = idx + 1  # Line numbers are 1-based
#                     print(f"Last modified line: {last_modified_line} (Line {line_number})")
#                     break
#
#
# def monitor_file(file_path):
#     # Set up watchdog
#     event_handler = FileModificationHandler(file_path)
#     observer = Observer()
#     observer.schedule(event_handler, os.path.dirname(file_path), recursive=False)
#
#     try:
#         observer.start()
#         print(f"Monitoring changes to: {file_path}")
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
#
#
# # Specify the file you want to monitor
# file_path = "D:\\new_env\\example.py"
# monitor_file(file_path)

import re
temp_stack = []
with open("D:\\new_env\\insist.html", "r+") as file:
    content = file.read()
    word_to_find = 'class=.*'
    matches = re.search(r'\b' + re.escape(word_to_find) + r'\b', content)
    # Regular expression to match HTML tags (both opening and closing)
    all_tags = re.compile(r'<(/?[a-zA-Z0-9]+)[^>]*>')
    # tag_pattern = re.compile(r'<([a-zA-Z0-9]+)[^>]*>')
    # closed_pattern = re.compile(r'</([a-zA-Z0-9]+)[^>]*>')
    class_tags = re.compile(r'<([a-zA-Z0-9]+)[^>]*\sclass="([^"]*)"')
    id_tags = re.compile(r'<([a-zA-Z0-9]+)[^>]*\sid="([a-zA-Z0-9]+)[^"]"')

    id_tags = re.findall(id_tags, content)
    class_tags = re.findall(class_tags, content)
    bb = re. findall(all_tags,content)
    print(id_tags, class_tags)
    empty = []
    stack = []
    var = ""
    print(bb)
    for i in bb:
        if i == "/html":
            break
        elif i == "meta":
            continue
        elif i[0] == "/":
            stack.pop()
        else:
            stack.append(i)
            var = " ".join(stack)
            print(var+"{}")





