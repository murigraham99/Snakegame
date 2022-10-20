from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_PACE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        n_segment = Turtle("square")
        n_segment.color("white")
        n_segment.penup()
        print(position)
        n_segment.goto(position)
        self.segments.append(n_segment)

    def extra_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for piece in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[piece - 1].xcor()
            new_y = self.segments[piece - 1].ycor()
            self.segments[piece].goto(new_x, new_y)
        self.segments[0].forward(MOVE_PACE)

    def up(self):
        for piece in self.segments:
            if piece.heading() == 0:
                piece.left(90)
            elif piece.heading() == 180:
                piece.right(90)
            elif piece.heading() == 270:
                pass

    def down(self):
        for piece in self.segments:
            if piece.heading() == 0:
                piece.right(90)
            elif piece.heading() == 180:
                piece.left(90)
            elif piece.heading() == 90:
                pass

    def left(self):
        for piece in self.segments:
            if piece.heading() == 0:
                pass
            if piece.heading() == 270:
                piece.right(90)
            elif piece.heading() == 90:
                piece.left(90)

    def right(self):
        for piece in self.segments:
            if piece.heading() == 180:
                pass
            elif piece.heading() == 270:
                piece.left(90)
            elif piece.heading() == 90:
                piece.right(90)

    def reset(self):
        for piece in self.segments:
            piece.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
