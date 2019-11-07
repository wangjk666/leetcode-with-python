def trapped(current, future, obstacles):
    print(current,future)
    for obstacle in obstacles:
        if current[0] == future[0] and current[0] == obstacle[0]:
            if current[1] < obstacle[1] < future[1]:
                future = [future[0], obstacle[1]-1]
            elif future[1] < obstacle[1] < current[1]:
                future = [future[0], obstacle[1]+1]
            else:
                continue
        elif current[1] == future[1] and current[1] == obstacle[1]:
            if current[0] < obstacle[0] < future[0]:
                future = [obstacle[0]-1, future[1]]
            elif future[0] < obstacle[0] < current[0]:
                future = [obstacle[0]+1, future[1]]
            else:
                continue
        else:
            continue
    print(future)
    return future


def robotSim(commands, obstacles):
    """
    :type commands: List[int]
    :type obstacles: List[List[int]]
    :rtype: int
    """
    dis = 0
    current = [0,0]
    d = ['n','e','s','w']
    dir = 0
    for command in commands:
        if  command == -1:
            dir = (dir + 1)%4
        elif command == -2:
            dir = (dir - 1 + 4)%4
        else:
            if dir == 0:
                future = [current[0], current[1]+command]
            elif dir == 1:
                future = [current[0]+command, current[1]]
            elif dir == 2:
                future = [current[0], current[1]-command]
            else:
                future = [current[0]-command, current[1]]
            current = trapped(current,future,obstacles)
            dt = pow(current[0],2) + pow(current[1],2)
            dis = max(dis,dt)
    return dis
        
class Robot:
    
    def __init__(self):
        self.directions = ['north', 'east', 'south', 'west']
        self.id = 0
        self.location = (0, 0)

    def turn_left(self):
        self.id = (self.id - 1) % 4

    def turn_right(self):
        self.id = (self.id + 1) % 4

    @property
    def direction(self):
        return self.directions[self.id]

    @property
    def dist_square(self):
        return sum(map(lambda x: x*x, self.location))

    def one_step(self, have_a_try=False):          # 向一个方向移动一步
        loc = self.location
        if self.direction == 'north':
            loc = self.location[0], self.location[1] + 1
        elif self.direction == 'east':
            loc = self.location[0] + 1, self.location[1]
        elif self.direction == 'south':
            loc = self.location[0], self.location[1] - 1
        elif self.direction == 'west':
            loc = self.location[0] - 1, self.location[1]
        if not have_a_try:
            self.location = loc
        return loc


class Solution:
    def robotSim(self, commands, obstacles):
        """
        :param commands: List[int]
        :param obstacles: List[List[int]]
        :return: int
        """

        robot = Robot()
        obstacles = set(map(tuple, obstacles))
        ans = 0                                     # 结果

        for cmd in commands:
            if cmd == -2:                           # 左转
                robot.turn_left()
            elif cmd == -1:                         # 右转
                robot.turn_right()
            else:
                for k in range(cmd):
                    if robot.one_step(have_a_try=True) in obstacles:
                        continue
                    else:
                        robot.one_step()
                        ans = max(ans, robot.dist_square)
        return ans

print(robotSim([4,-1,4,-2,4],[[2,4]]))