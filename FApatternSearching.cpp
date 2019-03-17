#include <bits/stdc++.h>

#define NO_OF_CHARS 256

using namespace std;

struct s {
    char *txt;
    char *pat;
};

int NextState(char *pat, int M, int state, int x) {
    if (state < M && x == pat[state]) return state + 1;
    int ns, i;

    for (ns = state; ns > 0; ns--) {
        if (pat[ns - 1] == x) {
            for (i = 0; i < ns - 1; i++)
                if (pat[i] != pat[state - ns + 1 + i]) break;
            if (i == ns - 1) return ns;
        }
    }
    return 0;
}

void computeTransitionFunction(char *pat, int M, int TF[][NO_OF_CHARS]) {
    int state, x;
    for (state = 0; state <= M; ++state)
        for (x = 0; x < NO_OF_CHARS; ++x)
            TF[state][x] = NextState(pat, M, state, x);
}

void search(char *pat, char *txt) {
    int M = strlen(pat);
    int N = strlen(txt);

    int TF[M + 1][NO_OF_CHARS];

    computeTransitionFunction(pat, M, TF);

    int i, state = 0;
    for (i = 0; i < N; i++) {
        state = TF[state][txt[i]];
        if (state == M) cout << "\n" << "String pattern found at index " << i - M + 1 << "\n\n";
    }
}

int main() {
    
    char txt[] = "ABAAAABAABAABAABABAAAB";
    char pat[] = "ABAAAB";
    
    search(pat, txt); //In params of search function use search(pattern of string, text of test case string)
    
    return 0;
}
