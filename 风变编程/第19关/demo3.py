start_floor = '3'
end_floor = '7'
floor_last_number = ['01','02','03']
start_floor_rooms = {301:[1,80],302:[1,80],303:[2,90]}
#初始楼层的模版数据
unit_rooms = {}
#新建一个存放所有楼层的字典
unit_rooms[int(start_floor)] = start_floor_rooms

for floor in range(int(start_floor) + 1, int(end_floor) + 1):
        #遍历除初始楼层外的其他楼层
        floor_rooms = {}
        #每个楼层都建立一个字典
        for i in range(len(start_floor_rooms)):
        #遍历每层有多少个房间，这里是3，即执行for i in range 3 的循环
            number = str(floor) + floor_last_number[i]
            info = start_floor_rooms[int(start_floor + floor_last_number[i])]
            # 依次取出字典start_floor_rooms键对应的值，即面积和朝向组成的列表
            floor_rooms[int(number)] = info
            #给字典floor_rooms添加键值对，floor_rooms = {401:[1,80]}
        unit_rooms[floor] = floor_rooms
print(unit_rooms)