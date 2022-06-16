import pygame
import sys


def check_win(mas, sign):
    dead_heat = 0
    for row in mas:
        dead_heat += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if dead_heat == 0:
        return 'Piece'
    return False


pygame.init()
size_box = 100  # размер кубика
margin = 15  # размер пропуска между кубиками
width = height = size_box * 3 + margin * 4  # ширина и высота окна исходя из значения кубика из пропусков

size_window = width, height
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-нолики')
black = (0, 0, 0,)
red = (178, 34, 34)
green = (50, 205, 50)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_box + margin)
            row = y_mouse // (size_box + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * size_box + (col + 1) * margin
                y = row * size_box + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_box, size_box))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_box - 5, y + size_box - 5), 3)
                    pygame.draw.line(screen, white, (x + size_box - 5, y + 5), (x + 5, y + size_box - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_box // 2, y + size_box // 2), size_box // 2 - 3, 3)

    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('stxingka', 80)
        text_1 = font.render(game_over, True, white)
        text_rect = text_1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text_1, [text_x, text_y])
    pygame.display.update()
