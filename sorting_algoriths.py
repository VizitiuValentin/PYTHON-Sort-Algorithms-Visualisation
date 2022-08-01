import pygame
import main
pygame.font.init()

def bubble_sort(array, anim_type):
    pygame.display.update()

    clock = pygame.time.Clock()
    comparatii = 0
    main.draw_sorting_screeen(array, comparatii)
    COMP_TEXT = pygame.font.SysFont("ARial", 20)

    flag = 1
    while flag == 1:
        clock.tick(main.FPS)
        main.draw_sorting_screeen(array, comparatii)
        text = COMP_TEXT.render("Total comparisons: " + str(comparatii) + "   Sorting algorithm: Bubble Sort", False, (255,255,255))
        main.WINDOW.blit(text, (0, 0))
        flag = 0

        for i, number in enumerate(array):
            if anim_type == 1:
                main.draw_sorting_screeen(array, comparatii)
                clock.tick(main.FPS)

            main.WINDOW.blit(text, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if i < 185:
                comparatii += 1
                if anim_type == 1:
                    main.WINDOW.blit(main.FILLER, (0, 0))
                    text = COMP_TEXT.render(
                        "Total comparisons: " + str(comparatii) + "   Sorting algorithm: Bubble Sort",
                        False, (255, 255, 255))
                    main.WINDOW.blit(text, (0, 0))

                if array[i] > array[i + 1]:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()

                    main.BIP.set_volume(number/100)
                    main.BIP.play()
                    temp = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = temp
                    flag = 1

        pygame.display.update()

def quick_sort(array, start, end, anim_type, comp):
    i, j = start, end
    temp = 0

    while i < j:
        while array[i] < array[end]:
            comp += 1
            i += 1
        while array[j] >= array[end] and j > i:
            j -= 1
            comp += 1

        if i != j:
            if anim_type == 1:
                main.draw_sorting_screeen(array, comp)
            main.BIP.set_volume(i/100 + 0.1)
            main.BIP.play()
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    main.draw_sorting_screeen(array, comp)

    temp = array[i]
    array[i] = array[end]
    array[end] = temp

    if i - start > 1:
        comp = quick_sort(array, start, i - 1, anim_type, comp)

    if end - i > 1:
        comp = quick_sort(array, i + 1, end, anim_type, comp)

    main.draw_sorting_screeen(array, comp)
    pygame.display.update()

    return comp

