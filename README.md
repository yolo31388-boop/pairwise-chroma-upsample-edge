# pairwise-chroma-upsample-edge

## 领域

游戏、图形与多媒体

## 主题

色度上采样与边缘

## 说明

双线性上采样、块对齐与矩阵权重。

初始状态下 `imaging/chroma_upsample_edge.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
