# sdu_zzl_class_project
2019级 201900460001张众良 课程作业

仅本人为一个小组，所有项目的简介以及具体说明在项目对应的文件夹中

## 完成的项目

Project: implement the naïve birthday attack of reduced SM3 （sm3 birthday attack）

Project: implement the Rho method of reduced SM3 （sm3 birthday attack）

以上两者写在同一个文件夹中

Project: implement length extension attack for SM3, SHA256, etc. （sm3 long extend attack）

Project: do your best to optimize SM3 implementation (software) （sm3）

Project: Impl Merkle Tree following RFC6962   （merkle trees）

Project: report on the application of this deduce technique in Ethereum with ECDSA  （ECDSA get PK）

Project: impl sm2 with RFC6979 （SM2_sign_RFC6979）

Project: verify the above pitfalls with proof-of-concept code （verify some pitfalls of ECDSA）

Project: Implement a PGP scheme with SM2 （sm2 PGP）

Project: forge a signature to pretend that you are Satoshi  （ECDSA forge sign）

Project: research report on MPT （research report on MPT）

## 未完成的项目

Project: Implement the above ECMH scheme

Project: implement sm2 2P sign with real network communication

Project: PoC impl of the scheme, or do implement analysis by Google

Project: implement sm2 2P decrypt with real network communication

Project: send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself

Project: Find a key with hash value “\*sdu_cst_20220610\*” under a message composed of \*your name\* followed by \*your student ID\*. For example, “\*San Zhan 202000460001\*”. 

Project: Find a 64-byte message under some  fulfilling that their hash value is symmetrical

Project Idea 1. Write a circuit to prove that your CET6 grade is larger than 425. a. Your grade info is like (cn_id, grade, year, sig_by_moe). These grades are published as commitments onchain by MoE. b. When you got an interview from an employer, you can prove to them that you have passed the exam without letting them know the exact grade. 2. The commitment scheme used by MoE is SHA256-based. a. commit = SHA256(cn_id, grade, year, sig_by_moe, r)
