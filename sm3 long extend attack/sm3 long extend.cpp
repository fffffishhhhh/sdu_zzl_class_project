// sm3 long extend.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

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
        s += '0';
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


string SM3Encrypt(string m,string secret="")
{
    m = secret + m;
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

string SM3LongExtend(string H_m,string m_1, string m_2, unsigned long long secret_size=0)
{
    unsigned long long size = (unsigned long long)m_1.size() * (unsigned long long)4+secret_size;
    unsigned long long last_lengh = size % 512;
    int Padding_lengh = PadMessage(m_1, last_lengh < 448 ? 448 - last_lengh : 960 - last_lengh, size);
    string temp = m_1 + m_2;
    
    unsigned long long size_temp = (unsigned long long)temp.size() * (unsigned long long)4+secret_size;
    unsigned long long last_lengh_temp = size_temp % 512;
    int Padding_lengh_t = PadMessage(m_2, last_lengh_temp < 448 ? 448 - last_lengh_temp : 960 - last_lengh_temp, size_temp);
    unsigned long long size_attack = (unsigned long long)m_2.size() * (unsigned long long)4;
    unsigned long long block_num = (size_attack) / 512;
    string* B = new string[block_num];
    string* V = new string[block_num + 1];
    V[0] = H_m;
    for (int i = 0; i < block_num; i++) {
        B[i] = m_2.substr(128 * i, 128);
        MessageExtend(B[i]);
        V[i + 1] = CF(V[i], B[i]);
    }
    return V[block_num];
}



unsigned long long Find_Secret_size(string H_m,string m_1,string m_2,string secret) //此处传入 secret 是为了模拟实际中对于服务器或者预言机的问询，并非直接的使用。
{
    for (int i = 0; i < 17; i+=4)
    {
        string m_1_copy = m_1;
        string m_2_copy = m_2;
        unsigned long long size = (unsigned long long)m_1_copy.size() * (unsigned long long)4 + i;
        unsigned long long last_lengh = size % 512;
        int Padding_lengh = PadMessage(m_1_copy, last_lengh < 448 ? 448 - last_lengh : 960 - last_lengh, size);
        string temp = m_1_copy + m_2_copy;
        if (SM3LongExtend(H_m, m_1, m_2, i) == SM3Encrypt(temp, secret))
        {
            cout << i;
            return i;
        }
    }
}

int main()
{
    string m_1 = "7380164914B2B9172442D7DA8A0600A96F30BC163138AAE38DEE4DB0E4E";
    string m_2 = "7380166F14B2B9172442D7DA8A0600A96F30BC163138AAE3E4DB0FB0E4E";
    string m_1_copy = m_1;
    string m_2_copy = m_2;
    string secret = "345";
    string H_m = SM3Encrypt(m_1, secret);
    unsigned long long Secret_size=Find_Secret_size(H_m, m_1, m_2, secret);
    unsigned long long real_size = (unsigned long long)secret.size() * (unsigned long long)4;    
    cout << (Secret_size == real_size);
    string H_attack = SM3LongExtend(H_m, m_1, m_2, Secret_size);
    unsigned long long size = (unsigned long long)m_1.size() * (unsigned long long)4 + real_size;
    unsigned long long last_lengh = size % 512;
    int Padding_lengh = PadMessage(m_1, last_lengh < 448 ? 448 - last_lengh : 960 - last_lengh, size);
    string temp = m_1 + m_2;
    string H_real = SM3Encrypt(temp, secret);
    cout << (H_attack == H_real);
}
