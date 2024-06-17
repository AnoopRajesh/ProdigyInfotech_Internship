#include <stdio.h>
#include <string.h>

int main() {
    char pwd[100];
    char str[20];
    char fb[5][100];
    int fbCnt;
    int len, u, l, d, s, met;

    while (1) {
        printf("Enter your password: ");
        scanf("%99s", pwd);

        len = strlen(pwd);
        u = l = d = s = 0;
        fbCnt = 0;

        // Check the length of the password
        if (len >= 8) {
            u = 1;
        } else {
            strcpy(fb[fbCnt++], "Password should be at least 8 characters long.");
        }

        // Check for uppercase, lowercase, digits, and special characters
        for (int i = 0; i < len; i++) {
            if (pwd[i] >= 'A' && pwd[i] <= 'Z') u = 1;
            if (pwd[i] >= 'a' && pwd[i] <= 'z') l = 1;
            if (pwd[i] >= '0' && pwd[i] <= '9') d = 1;
            if ((pwd[i] >= '!' && pwd[i] <= '/') || 
                (pwd[i] >= ':' && pwd[i] <= '@') || 
                (pwd[i] >= '[' && pwd[i] <= '`') || 
                (pwd[i] >= '{' && pwd[i] <= '~')) s = 1;
        }

        // Provide feedback for missing criteria
        if (!u) {
            strcpy(fb[fbCnt++], "Password should include at least one uppercase letter.");
        }
        if (!l) {
            strcpy(fb[fbCnt++], "Password should include at least one lowercase letter.");
        }
        if (!d) {
            strcpy(fb[fbCnt++], "Password should include at least one number.");
        }
        if (!s) {
            strcpy(fb[fbCnt++], "Password should include at least one special character.");
        }

        // Determine the strength of the password
        met = u + l + d + s;

        if (met == 4 && len >= 8) {
            strcpy(str, "Very Strong");
        } else if (met == 4) {
            strcpy(str, "Strong");
        } else if (met == 3) {
            strcpy(str, "Medium");
        } else if (met == 2) {
            strcpy(str, "Weak");
        } else {
            strcpy(str, "Very Weak");
        }

        printf("Password Strength: %s\n", str);
        if (fbCnt > 0) {
            printf("Feedback:\n");
            for (int i = 0; i < fbCnt; i++) {
                printf("- %s\n", fb[i]);
            }
        }

        if (strcmp(str, "Very Strong") == 0) {
            break;
        }
    }

    return 0;
}

