#include <iostream>
#include <string>
using namespace std;


string IV = "7380166F4914B2B9172442D7DA8A0600A96F30BC163138AAE38DEE4DB0FB0E4E";
unsigned int Tj[2] = { 0x79cc4519, 0x7a879d8a };
string hex_num = "0123456789ABCDEF";
unsigned int* Extend_m_1 = new unsigned int[68];
unsigned int* Extend_m_2 = new unsigned int[64];


unsigned int cir_left(unsigned int num, int left)   // 循环左移
{             
    return (num << left) | (num >> (32 - left));
}
unsigned int find_Tj(int x)     //得到常数 T_j
{                                 
    return x > 15 ? Tj[1] : Tj[0];
}
unsigned int FFi(unsigned int x, unsigned int y, unsigned int z, int n) {  
    return n > 15 ? ((x & y) | (y & z) | (x & z)) : (x ^ y ^ z);
}
unsigned int GGi(unsigned int x, unsigned int y, unsigned int z, int n) {
    return n > 15 ? ((x & y) | ((~x) & z)) : (x ^ y ^ z);
}
unsigned int P_0(unsigned int x) {  
    return (x ^ cir_left(x, 9) ^ cir_left(x, 17));
}
unsigned int P_1(unsigned int x) {
    return (x ^ cir_left(x, 15) ^ cir_left(x, 23));
}

uint32_t str2uint(string s) {    //字符串转32位
    uint32_t temp = 0;
    for (auto i : s)
        temp = ((temp << 4) | (i < 58 ? i - 48 : i - 55));
    return temp;
}
string uint2str(unsigned int num, int k = 8, string s = "")   // 32位转字符串
{
    for (int i = 0; i < k; i++, num /= 16)
        s += hex_num[num % 16];
    return string(s.rbegin(), s.rend());
}

int PadMessage(string& s, int n, unsigned long long size)    //消息填充
{   
    s += '8';
    for (int i = 0; i < (n / 4 - 1); i++)
        s+='0';
    string ss = uint2str(size, 16);
    s += ss;
    return n;
}

void MessageExtend(string B_i) 
{
    for (int i = 0; i < 16; i++)
        Extend_m_1[i] = str2uint(B_i.substr(8 * i, 8));
    for (int i = 16; i < 68; i++) {
        Extend_m_1[i] = (P_1(Extend_m_1[i - 16] ^ Extend_m_1[i - 9] ^ cir_left(Extend_m_1[i - 3], 15)) ^ cir_left(Extend_m_1[i - 13], 7) ^ Extend_m_1[i - 6]);
    }
    for (int i = 0; i < 64; i++)
        Extend_m_2[i] = (Extend_m_1[i] ^ Extend_m_1[i + 4]);
}

string CF(string V, string Bi) 
{
    unsigned int ABCDEFGH[8];
    unsigned int vi[8];
    for (int i = 0; i < 8; i++) {
        ABCDEFGH[i] = str2uint(V.substr(8 * i, 8));
        vi[i] = ABCDEFGH[i];
    }
    for (int i = 0; i < 64; i++) {
        unsigned int SS1 = cir_left((cir_left(ABCDEFGH[0], 12) + ABCDEFGH[4] + cir_left(find_Tj(i), i % 32)), 7);
        unsigned int SS2 = (SS1 ^ cir_left(ABCDEFGH[0], 12));
        unsigned int TT1 = FFi(ABCDEFGH[0], ABCDEFGH[1], ABCDEFGH[2], i) + ABCDEFGH[3] + SS2 + Extend_m_2[i];
        unsigned int TT2 = GGi(ABCDEFGH[4], ABCDEFGH[5], ABCDEFGH[6], i) + ABCDEFGH[7] + SS1 + Extend_m_1[i];
        ABCDEFGH[3] = ABCDEFGH[2]; ABCDEFGH[2] = (cir_left(ABCDEFGH[1], 9)); ABCDEFGH[1] = ABCDEFGH[0];
        ABCDEFGH[0] = TT1; ABCDEFGH[7] = ABCDEFGH[6]; ABCDEFGH[6] = cir_left(ABCDEFGH[5], 19); ABCDEFGH[5] = ABCDEFGH[4]; ABCDEFGH[4] = P_0(TT2);
    }
    string result = "";
    for (int i = 0; i < 8; i++)
        result += uint2str(vi[i] ^ ABCDEFGH[i]);
    return result;
}


string SM3Encrypt(string m)
{
    unsigned long long size = (unsigned long long)m.size() * (unsigned long long)4;
    unsigned long long last_lengh = size % 512;
    int Padding_lengh = PadMessage(m, last_lengh < 448 ? 448 - last_lengh : 960 - last_lengh, size);
    unsigned long long block_num = (size + 64 + Padding_lengh) / 512;
    string* B = new string[block_num];
    string* V = new string[block_num + 1];
    V[0] = IV;
    for (int i = 0; i < block_num; i++) {
        B[i] = m.substr(128 * i, 128);
        MessageExtend(B[i]);
        V[i + 1] = CF(V[i], B[i]);
    }
    return V[block_num];
}

int main()
{
    string m = "73866F491172442D7A8A0600A96F30BC163138AAE38DEE4DB0FB0E4E";
    cout << SM3Encrypt(m);
}