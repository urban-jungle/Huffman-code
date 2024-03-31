#동국대학교 정보통신공학과 2019112110 이정민
import heapq

class Node:
    def __init__(self, probability, value=None):
        self.probability = probability
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.probability < other.probability # 확률이 더 낮은 노드가 더 작은 것으로 간주

def build_minimum_variance_huffman_code(probabilities):
    pq = [Node(p, letter) for p, letter in zip(probabilities, ["A", "B", "C", "D"]) if p > 0]
    heapq.heapify(pq)

    while len(pq) > 1:
        # 가장 확률이 낮은 두 노드를 선택합니다.
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        # right가 None이거나 left의 길이가 더 작을 경우에 left와 right를 바꿉니다.
        if right is None or (left is not None and (right.value is None or (left.value is not None and len(left.value) <= len(right.value)))):
            merged = Node(left.probability + right.probability)
            merged.left = left
            merged.right = right
        else:
            merged = Node(left.probability + right.probability)
            merged.left = right
            merged.right = left
        heapq.heappush(pq, merged)

    huffman_root = pq[0]
    codes = {}
    build_code(huffman_root, codes, "")
    return codes

def build_code(node, codes, code):
    if node is None:
        return
    if node.value is not None:
        codes[node.value] = code
    else:
        build_code(node.left, codes, code + "0")
        build_code(node.right, codes, code + "1")

# 주어진 확률
probabilities = [0.42857142857142857142857142857143, 0.14285714285714285714285714285714, 0.14285714285714285714285714285714, 0.28571428571428571428571428571429]

# Minimum Variance 허프만 코드 생성
codes = build_minimum_variance_huffman_code(probabilities)

# 결과 출력
for letter, code in sorted(codes.items()):
    print(f"Letter: {letter}, Huffman Code: {code}")