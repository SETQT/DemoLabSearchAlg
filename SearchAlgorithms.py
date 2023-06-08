from ast import Del
from audioop import add
from cmath import exp
from pickle import FALSE, TRUE
from symbol import for_stmt
from Space import *
from Constants import *
import math




def isAllNeiborVisited(n: Node, list, g: Graph):

    neibor = g.get_neighbors(n)
    for item in neibor:
        if (item is not None and item not in list):
            return FALSE
    return TRUE


def drawLine(n: Node, n2: Node, sc: pygame.Surface):
 
    pygame.draw.line(sc, green, (n.x, n.y), (n2.x, n2.y), 2)
    pygame.display.flip()



def DFS(g: Graph, sc: pygame.Surface):
   

    list = []
    visited = []

    list.append(g.start)

    while(list):

        node = list.pop()
        check = FALSE

        g.update(yellow, node.value, sc)

        if (node == g.goal):
            break
        neibor = g.get_neighbors(node)
        neibor.reverse()
        if (node not in visited):
            visited.append(node)
            
            for item in neibor:
                if (item is not None and item not in visited):
                    check = TRUE
                    list.append(item)
                    # list.insert(0, 100)
                    g.update(red, item.value, sc)
        if not check:
            visited.pop()
        g.update(blue, node.value, sc)
    if (node.value!=g.goal.value):
            return "not found"
    visited.reverse()
    head = g.goal
    g.update(purple, g.goal.value, sc)
    g.update(orange, g.start.value, sc)
    for i in range(0, len(visited)):

        if visited[i] != g.start:
            g.update(grey, visited[i].value, sc)
        drawLine(visited[i], head, sc)
        head = visited[i]
       


def BFS(g: Graph, sc: pygame.Surface):

    father = [-1]*g.get_len()

    close = []
    list = []
  
    list.append(g.start)
   
    while (list):
        node = list[0]
        del list[0]
        g.update(yellow, node.value, sc)

        # print(node.value)
        if (node.value == g.goal.value):
            break

        if (node not in close):
            close.append(node)
            neibor = g.get_neighbors(node)
     

            for item in neibor:
                if (item is not None and item not in list and item not in close):
                    father[item.value] = node
                    list.append(item)
                 
                    g.update(red, item.value, sc)
        g.update(blue, node.value, sc)

    if (node.value!=g.goal.value):
        return "not found"
   
    head = father[g.goal.value]
    g.update(purple, g.goal.value, sc)
    g.update(orange, g.start.value, sc)
    drawLine(head, g.goal, sc)

    while (head.value != g.start.value):
        g.update(grey, head.value, sc)
        drawLine(head, father[head.value], sc)
        head = father[head.value]


def minDistanceCost(node1: Node, node2: Node):
   
    dis = math.sqrt(pow(node1.x - node2.x, 2) + pow(node1.y - node2.y, 2))
    return dis


def UCS(g: Graph, sc: pygame.Surface):

    father = [-1]*g.get_len()
    cost = [0]*g.get_len()
    cost[g.start.value] = 0
    close = []
    explored = []
    explored.append(g.start)
    node = explored[0]
    while (list):
        g.update(yellow, node.value, sc)
       
        if (node.value == g.goal.value):
            break
        if (node not in close):
            close.append(node)
        neibor = g.get_neighbors(node)
        for item in neibor:
            if (item is not None and item not in close):
                if item not in explored:
                    explored.append(item)
                    father[item.value] = node
                    g.update(red, item.value, sc)
                    cost[item.value] = minDistanceCost(
                        item, node)+cost[node.value]
                else:
                    if cost[item.value] > minDistanceCost(item, node)+cost[item.value]:
                        cost[item.value] = minDistanceCost(item, node)+cost[item.value]
                        father[item.value] = node
        g.update(blue, node.value, sc)
        index = cost[explored[0].value]
        min = explored[0]
        for i in explored:
            if cost[i.value] < index:
                index = cost[i.value]
                min = i
        node = min
        explored.remove(node)
    if (not list):
        return "not found"

    head = father[g.goal.value]
    g.update(purple, g.goal.value, sc)
    g.update(orange, g.start.value, sc)
    drawLine(head, g.goal, sc)

    while (head.value != g.start.value):
        g.update(grey, head.value, sc)
        drawLine(head, father[head.value], sc)
        head = father[head.value]




def AStar(g: Graph, sc: pygame.Surface):

  
    father = [-1]*g.get_len()

    cost = [0]*g.get_len()
    cost[g.start.value] = 0

    close = []
    explored = []
    explored.append(g.start)
    node = explored[0]

    while (list):
      
        g.update(yellow, node.value, sc)
       
        if (node.value == g.goal.value):
            break
        if (node not in close):
            close.append(node)
        neibor = g.get_neighbors(node)
       
        explored.pop()
        for item in neibor:
            if (item is not None and item not in close):
                if item not in explored:
                   
                    explored.append(item)
                    g.update(red, item.value, sc)
                    father[item.value] = node
                    cost[item.value] = minDistanceCost( item, node)+ minDistanceCost( item, g.goal)
                else:
                    if cost[item.value] > minDistanceCost(item, node)+cost[item.value]+ minDistanceCost( item, g.goal):
                        cost[item.value] = minDistanceCost(item, node)+cost[item.value] + minDistanceCost( item, g.goal)
                        father[item.value] = node
        g.update(blue, node.value, sc)
        index = cost[explored[0].value]
        min = explored[0]
        for i in explored:
            if cost[i.value] < index:
                index = cost[i.value]
                min = i
        node = min
        explored.remove(node)
    if (not list):
        return "not found"

    close.reverse()
    head = father[g.goal.value]
    g.update(purple, g.goal.value, sc)
    g.update(orange, g.start.value, sc)
    drawLine(head, g.goal, sc)

    while (head.value != g.start.value):
        g.update(grey, head.value, sc)
        drawLine(head, father[head.value], sc)
        head = father[head.value]

  
