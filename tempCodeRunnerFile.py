    # Bird
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface,bird_rect)
        check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list )