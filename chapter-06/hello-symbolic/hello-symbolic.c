#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
	printf("Option: \n");
	char c = getchar();
	if (c > 64) {
		if (c < 91) {
            // input must be an upper-case alphabetical character
			printf("hello\n");
			return 0;
		} else {
			printf("how are you\n");
			return 1;
		}
	}
	
	printf("bye\n");
	return 1;
}