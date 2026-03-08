"""
thoughtSignature 处理公共模块

提供统一的 thoughtSignature 编码/解码功能，用于在工具调用ID中保留签名信息。
这使得签名能够在客户端往返传输中保留，即使客户端会删除自定义字段。
"""

from typing import Optional, Tuple

# 在工具调用ID中嵌入thoughtSignature的分隔符
# 这使得签名能够在客户端往返传输中保留，即使客户端会删除自定义字段
THOUGHT_SIGNATURE_SEPARATOR = "__thought__"


def encode_tool_id_with_signature(tool_id: str, signature: Optional[str]) -> str:
    """
    为了避免 OpenAI 兼容客户端（如 Cursor、Kilocode）截断过长的 tool_call_id，
    我们不再将 thoughtSignature 编码到 ID 中。
    相反，后续将始终使用官方提供的免验证占位符 context_engineering_is_the_way_to_go。

    Args:
        tool_id: 原始工具调用ID
        signature: thoughtSignature（不再使用）

    Returns:
        仅返回原始工具调用ID
    """
    return tool_id


def decode_tool_id_and_signature(encoded_id: str) -> Tuple[str, Optional[str]]:
    """
    为了兼容旧版本的编码ID，尝试提取真实的ID，并始终返回 None 作为签名。
    这样强制后续使用免验证占位符。
    
    Args:
        encoded_id: 编码的工具调用ID

    Returns:
        (原始工具ID, None)
    """
    if not encoded_id or THOUGHT_SIGNATURE_SEPARATOR not in encoded_id:
        return encoded_id, None
    parts = encoded_id.split(THOUGHT_SIGNATURE_SEPARATOR, 1)

    return parts[0], None
