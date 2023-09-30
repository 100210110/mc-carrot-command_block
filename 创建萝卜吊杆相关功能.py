from pyperclip import copy


def command_out(run_command, text):     # 套上检测再复制
    command = f"""/execute as @a[nbt={{SelectedItem:{{tag:{{Re_tool:{tool_name}}}}}}},scores={{carrot_used=1..}}] at @s run {run_command}"""
    print(command, f"\n\n<{text}已复制>")
    copy(command)
    input(f"-按任意键继续-\n")

def command_copy(run_command, text):    # 直接复制
    print(run_command, f"\n\n<{text}已复制>")
    copy(run_command)
    input(f"-按任意键继续-\n")



default_tool_name = "Re_tool"
default_item_name = "物品名字"
default_name_color = "gold"
default_name_italic = "false"
default_name_bold = "true"
default_Lore_text1 = "这是默认物品功能描述"
default_Lore_color1 = "aqua"
default_Lore_italic1 = "false"
default_Lore_text2 = "这是默认吐槽"
default_end_command = "scoreboard players reset @a[scores={carrot_used=1..}] carrot_used"


mode = 0
while True:     # 选择模式
    try:
        mode = int(input("输入模式(1.只自定义字符, 2.自定义所有格式): "))
        if 1 <= mode <= 2:
            break
        else:
            print("超出范围")
            continue
    except ValueError:
        print("这不是合法的数字")

if mode == 1:
    name_color = default_name_color
    name_italic = default_name_italic
    name_bold = default_name_bold
    Lore_color1 = default_Lore_color1
    Lore_italic1 = default_Lore_italic1
    tool_name = input(f"Re_tool命名 (默认{default_tool_name}):") or default_tool_name
    item_name = input(f"物品名字 (默认{default_item_name}): ") or default_item_name
    Lore_text1 = input(f"物品功能描述 (默认{default_Lore_text1}): ") or default_Lore_text1
    Lore_text2 = input(f"物品吐槽 (默认{default_Lore_text2}): ") or default_Lore_text2
    print()
elif mode == 2:
    tool_name = input(f"Re_tool命名 (默认{default_tool_name}):") or default_tool_name
    item_name = input(f"物品名字 (默认{default_item_name}): ") or default_item_name
    name_color = input(f"颜色 (默认{default_name_color}): ") or default_name_color
    name_italic = input(f"斜体 (默认{default_name_italic}): ") or default_name_italic
    name_bold = input(f"加粗 (默认{default_name_bold}): ") or default_name_bold
    Lore_text1 = input(f"物品功能描述 (默认{default_Lore_text1}): ") or default_Lore_text1
    Lore_color1 = input(f"颜色 (默认{default_Lore_color1}): ") or default_Lore_color1
    Lore_italic1 = input(f"斜体 (默认{default_Lore_italic1}): ") or default_Lore_italic1
    Lore_text2 = input(f"物品吐槽 (默认{default_Lore_text2}): ") or default_Lore_text2
    print()
    
give_command = f"""/give @p minecraft:carrot_on_a_stick{{Re_tool:{tool_name},display:{{Name:'{{"text":"{item_name}","color":"{name_color}","italic":{name_italic},"bold":{name_bold}}}',Lore:['{{"text":"{Lore_text1}","color":"{Lore_color1}","italic":{Lore_italic1}}}','{{"text":"{Lore_text2}"}}']}}}}"""
command_copy(give_command, f"获取物品指令")

title_command = f"""title @s actionbar [{{"text":"","bold":"true"}},{{"text":"<","color":"yellow"}},{{"text":"{item_name}","color":"gold"}},{{"text":">","color":"yellow"}},{{"text":" 当前已","color":"yellow"}},{{"text":" 开启","color":"green"}}]"""
befor_command = f"""/execute as @a[nbt={{SelectedItem:{{tag:{{Re_tool:{tool_name}}}}}}}] at @s run {title_command}"""
command_copy(befor_command, "状态为开的通知")

text_command = f"""tellraw @s [{{"text":">>> ","bold":true,"color":"yellow"}},{{"text":"当前已执行 ","color":"white","bold":"false"}},{{"text":"{item_name}","color":"green"}}]"""
command_out(text_command, "执行文本反馈指令")

sound_command = """playsound minecraft:block.note_block.bell voice @s ~ ~ ~"""
command_out(sound_command, "执行声音反馈指令")

i = 1
run_command = input(f"第 {i} 条指令为")
while run_command:
    command_out(run_command, f"第 {i} 次进行指令")    
    i += 1
    run_command = input(f"第 {i} 条指令为")
    

end_command = default_end_command
command_out(end_command, "结束指令")

title_command = f"""title @s actionbar [{{"text":"","bold":"true"}},{{"text":"<","color":"yellow"}},{{"text":"{item_name}","color":"gold"}},{{"text":">","color":"yellow"}},{{"text":" 当前已","color":"yellow"}},{{"text":" 关闭","color":"red"}}]"""
ending_command = f"""/execute as @a[nbt={{SelectedItem:{{tag:{{Re_tool:{tool_name}}}}}}}] at @s run {title_command}"""
copy(ending_command)
print(ending_command, f"\n\n<状态为关的通知已复制>")
input(f"-按任意键结束-\n")