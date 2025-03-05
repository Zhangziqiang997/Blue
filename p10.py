
# (m^k)mod p
def fast_power(base, exponent, mod):
    """
    快速幂算法，计算 (base^exponent) % mod
    :param base: 底数
    :param exponent: 指数
    :param mod: 模数
    :return: 结果 (base^exponent) % mod
    """
    result = 1  # 初始化结果为1
    current_base = base % mod  # 初始底数，模 mod 避免大数
    current_exponent = exponent  # 保存原始指数，便于调试查看
    
    print(f"计算 {base}^{exponent} % {mod}")
    while exponent > 0:
        if exponent & 1:  # 如果当前指数最低位是1
            result = (result * current_base) % mod  # 累乘当前底数
            print(f"当前指数 {exponent}，最低位为1，更新结果 result = {result}")
        current_base = (current_base * current_base) % mod  # 更新底数为其平方
        print(f"更新底数 current_base = {current_base}")
        exponent >>= 1  # 右移一位，相当于指数除以2
        print(f"指数右移后 exponent = {exponent}")
    
    print(f"最终结果: {result}")
    return result


# 测试例子
base = 7
exponent = 15
mod = 9
result = fast_power(base, exponent, mod)
print(f"\n{base}^{exponent} % {mod} = {result}")