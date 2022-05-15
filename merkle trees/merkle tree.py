import hashlib
import random


class Merkletree(object):
    def __init__(self):
        self.leaves = list()
        self.levels = None
        self.well_prepared = False

    def add_leaf(self, leaf_Values, do_hash=False):  # 将所有要加入的叶结点存入列表
        self.well_prepared = False
        # 检查是不是单节点
        if not isinstance(leaf_Values, tuple) and not isinstance(leaf_Values, list):
            leaf_Values = [leaf_Values]
        for v in leaf_Values:
            v = '0x00' + v
            v = v.encode('utf-8')
            v = hashlib.sha256(v).hexdigest()
            v = bytearray.fromhex(v)
            self.leaves.append(v)

    def _calculate_up(self):
        Separate_leave = None
        N = len(self.levels[0])  # 该层节点数量
        if N % 2 == 1:  # 如果这层是奇数个节点
            Separate_leave = self.levels[0][-1]
            N -= 1
        new_level = []
        # 将节点两两配对
        for l, r in zip(self.levels[0][0:N:2], self.levels[0][1:N:2]):
            new_level.append(hashlib.sha256(bytearray(0x01) + l + r).digest())
        # 如果有单一节点，则把它放在最后面
        if Separate_leave is not None:
            new_level.append(Separate_leave)
        self.levels = [new_level, ] + self.levels

    def make_tree(self):
        self.well_prepared = False
        if len(self.leaves) > 0:
            self.levels = [self.leaves, ]
            while len(self.levels[0]) > 1:
                self._calculate_up()
        self.well_prepared = True

    def get_merkle_root(self):
        if self.well_prepared:
            if self.levels is not None:
                return (self.levels[0][0]).hex()
            else:
                return None
        else:
            return None

    # 获得证明链
    def get_evidence(self, index):
        if self.levels is None:
            return None
        elif not self.well_prepared or index > len(self.leaves) - 1 or index < 0:
            return None
        else:
            evidence = []
            for x in range(len(self.levels) - 1, 0, -1):  # 自底向上遍历
                level_len = len(self.levels[x])  # 获取当前层节点数量
                if (index == level_len - 1) and (level_len % 2 == 1):  # 如果要取证的是单一节点，则在这一层找不到它的兄弟
                    index = int(index / 2.)  # 直接跳到上一层
                    continue
                is_right_node = index % 2  # 判断所求证的节点是左节点还是右节点
                if is_right_node:  # 以此得到它兄弟节点的位置和索引
                    sibling_index = index - 1
                    sibling_pos = "left"
                else:
                    sibling_index = index + 1
                    sibling_pos = "right"
                sibling_value = (self.levels[x][sibling_index]).hex()
                evidence.append((sibling_pos, sibling_value))
                index = int(index / 2.)
            return evidence

            # 存在性证明:用由索引得到的证明链对得到的hash值进行校验

    def validate_proof(self, evidence, target_hash, merkle_root):
        merkle_root = bytearray.fromhex(merkle_root)
        target_hash = bytearray.fromhex(target_hash)
        if len(evidence) == 0:
            return target_hash == merkle_root
        else:
            proof_hash = target_hash
            for p in evidence:
                pos = p[0]
                sibling_value = bytearray.fromhex(p[1])
                if pos == 'left':
                    proof_hash = hashlib.sha256(bytearray(0x01) + sibling_value + proof_hash).digest()
                else:
                    proof_hash = hashlib.sha256(bytearray(0x01) + proof_hash + sibling_value).digest()
            print('计算出的根节点哈希：', proof_hash)
            print('正确的根节点哈希：', merkle_root)
            return proof_hash == merkle_root

    def travel(self):
        if self.levels is None:
            return None
        else:
            f = open('travel.txt', 'w')
            for x in range(len(self.levels)):  # 自顶向下遍历
                level_len = len(self.levels[x])  # 广度优先遍历
                str1 = 'level:' + str(x) + '\n'
                f.write(str1)
                for y in range(level_len):
                    str2 = 'order:' + str(y) + '     hash:  ' + str((self.levels[x][y]).hex()) + '\n'
                    f.write(str2)
            f.close()
        return


if __name__ == '__main__':
    values = []
    for i in range(100000):
        values.append(str(i))
    MT = Merkletree()
    MT.__init__()
    MT.add_leaf(values)
    MT.make_tree()
    root = MT.get_merkle_root()
    MT.travel()

    # 随机选择一叶节点验证其哈希值是否正确
    target = random.randint(0, 99999)
    evidence = MT.get_evidence(target)
    target_hash = (MT.levels[-1][target]).hex()
    print('校验路径为：', evidence)
    print(MT.validate_proof(evidence, target_hash, root))
