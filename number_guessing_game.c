#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int num, no_of_guess = 1, guess;

    srand(time(0));
    num = rand() % 100 + 1;

    printf("This is a game of guessing the correct number that computer has choosen\n\n");
    printf("Guess the number between 1 to 100 : \n");

    do
    {
        if (no_of_guess > 10)
        {
            printf("\nYou have attempted maximum 10 attempts .... GAME OVER ");
            goto end;
            break;
        }

        scanf("%d", &guess);

        if (guess > num)
        {
            printf("Lower number please !! \n");
        }

        else if (guess < num)
        {
            printf("Higher number please !!\n");
        }

        else
        {
            printf("You guessed the correct number in %d attempts\n", no_of_guess);
        }

        no_of_guess++;

    } while (guess != num);

    end :
    printf("\n\nThe correct answer is = %d", num);

    return 0;
}
