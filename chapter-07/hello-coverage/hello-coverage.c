#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char command[100];

    if (argc < 2) {
        return 1;
    }

    if (strcmp(argv[1], "hello") == 0) {
        if (argc != 3) {
            return 1;
        }
        snprintf(command, sizeof(command), "echo Hello, %s", argv[2]);
        system(command);
    } else if (strcmp(argv[1], "bye") == 0) {
        printf("bye bye\n");
    } else {
        printf("Invalid option\n");
    }

    return 0;
}