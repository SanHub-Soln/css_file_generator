import re
file_path = r"your_path\FILE.CSS"

output_path = os.path.join(os.path.dirname(file_path), "index.css")

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    bb = re.findall(r'<(/?[a-zA-Z0-9]+)([^>]*)>', content)
    hub=''
    stack = []
    nth = 1
    child = ":nth-child"
    waited_area = []
    waste = ["html"," body"]
    var = ""
with open(output_path, "w", encoding="utf-8") as outfile:
    outfile.write("""\
    :root {}
    html {}
    body {}
    @media screen and (max-width: 600px) {}
    
    @media screen and (max-width: 600px) {
      /* Styles for phones */
    }
    
    @media screen and (min-width: 601px) and (max-width: 768px) {
      /* Styles for tablets */
    }
    
    @media screen and (min-width: 769px) and (max-width: 1024px) {
      /* Styles for small laptops/desktops */
    }
    
    @media screen and (min-width: 1025px) {
      /* Styles for large desktops */
    }
    """)

    for i in bb:
        tagname, attributes = i
        id_match = re.findall(r'id\s*=\s*"([^"]+)"' ,attributes)
        class_match = re.findall(r'class\s*=\s*"([^"]+)"', attributes)
        r = len(stack)
        if tagname == "/html":
                break
        elif tagname in ["meta", "link"] or (tagname in  waste):
                continue
        elif tagname.startswith('/'):
            poped = stack.pop()
        elif id_match:
            data = f'#{id_match[0]}'
            stack.append(data)
            id_match, class_match = [], []
        elif class_match:
            data = f'.{class_match[0]}'
            stack.append(data)
            id_match, class_match = [], []
        
        elif nth > 1:
                if (tagname != waited_area):
                    nth = 1
                    waited_area= tagname
                    stack.append(tagname)
                else:
                    nth +=1
                    ans = f'{tagname +child}({nth})'
                    stack.append(ans)
        else:
            if tagname != waited_area:
                nth = 1
                waited_area = tagname
                stack.append(waited_area)
            else:
                waited_area = tagname
                hub = f'{tagname +child}({nth+1})'
                stack.append(f'{tagname +child}({nth})')
                nth+=1
        if r != len(stack) and not(tagname.startswith('/')):
           var = " ".join(stack)  
           outfile.write(f"{var} {{}}")
           if hub:
                outfile.write(" ".join(stack[:-1])+" "+hub+" {}")
                hub = ""
