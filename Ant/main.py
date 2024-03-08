from PIL import Image
from classes import Field, Ant


def main():
    field = Field((1024, 1024))

    # координаты центра поля, для начального положения муравья
    x, y = map(lambda coord: int(coord / 2 - 1), field.cells.shape)
    ant = Ant(x, y)
    while all(map(lambda cord: 0 < cord < 1023, (x, y))):
        x, y = ant.x, ant.y
        if field.cells[x][y] == 0:
            ant.turn(right=False)
        else:
            ant.turn()
        field.invertion(x, y)

        if ant.position in (0, 180):
            y += ant.position // 90 - 1

        elif ant.position in (90, 270):
            x += 270 // ant.position - 2
        ant.x = x
        ant.y = y

    black_cells_amount = 1024 * 1024 - sum(field.cells.ravel())
    # black_cells_amount = len(list(filter(lambda x: x == 0, field.cells.ravel())))

    i = Image.fromarray(field.cells)
    i.save('ant_track.bmp')


if __name__ == '__main__':
    main()
