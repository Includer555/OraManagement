import datetime

#TITLE
def WriteTitle():
    print("-------------------------------------------------------------")
    print("|             📁📋Work Hour Management📋📁                |")
    print("-------------------------------------------------------------\n\n")

def SaveWorkTime(anwser):
    f = open("Management.txt", "a")
    f.write(f"{datetime.datetime.today().strftime('%Y-%m-%d')} {anwser}\n");
    print(f"[📥] Saved: {datetime.datetime.today().strftime('%Y-%m-%d')} {anwser}")
    print("-------------------------------------------------------------")
    f.close()

anwser = 0

def DeleteAllData():
    f = open("Management.txt", "w")
    f.write("")
    f.close()

def ShowInfo():
    f = open("Management.txt", "r")
    print("-------------------------ALL HOURS---------------------------")
    lines = f.readlines()
    for idx, line in enumerate(lines, start=1):
        processed_line = line.strip()
        print(f"[📜] {idx}. {processed_line}")
    print("-------------------------------------------------------------")

def CalculateAllTime():
    lines = []
    f = open("Management.txt", "r")
    for line in f:
        processed_line = line.strip()
        lines.append(processed_line)
    f.close()

    sum = 0

    if(len(lines) > 0):
        for line in lines:
            splitted_line = line.split()
            sum += int(int(splitted_line[1]))
    
    return f"--------------------------ALL HOURS--------------------------\n{sum} Óra"

def RemoveLine():
    lines = []
    ShowInfo()
    remove_line = int(input("[❓] Line to remove : "))
    f = open("Management.txt", "r")
    for line in f:
        processed_line = line.strip()
        lines.append(processed_line)

    f.close()
    
    try:
        deleted_line = f"{lines[remove_line-1]}"
        del lines[remove_line-1]
        lines_to_write = ""
        for line in lines:
            lines_to_write += line+"\n"
        f = open("Management.txt", "w")
        f.write(lines_to_write)
        f.close()
        ShowInfo()
        print(f"[✅] Removed {deleted_line}")
        print("-------------------------------------------------------------")
    except:
        f.close()
        print("[❌] Enter a valid line!")
        print("-------------------------------------------------------------")
    

while anwser != 1:
    WriteTitle()
    try:
        anwser = int(input("[❓] 1.Exit \n[❓] 2.Hour Management \n[❓] 3.Show Info \n[❓] 4.Remove Line \n[❓] 5.Erase all data \n[❓] 6. Sum all data \n[❓] Anwser: "))

        match (anwser):
            case 1:
                break
            case 2:
                print("-------------------------------------------------------------")
                hours = int(input("[❓] Hour? : "))
                SaveWorkTime(hours)
            case 3:
                ShowInfo()
            case 4:
                RemoveLine()
            case 5:
                DeleteAllData()
            case 6:
                print(CalculateAllTime())
    except:
        print("[❌] Enter only a number!")