#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
关键词分类处理脚本
处理 keyword1.csv 和 keyword2.csv，添加分类列并按分类排序
"""

import pandas as pd
import re
import os

def classify_keyword(keyword):
    """
    根据关键词内容进行分类
    
    Args:
        keyword (str): 关键词字符串
        
    Returns:
        str: 分类标签
    """
    keyword_lower = keyword.lower()
    
    # 1. 注册相关 (Registration)
    registration_patterns = [
        r'注册', r'register', r'账号创建', r'开通', r'怎么.*注册', r'如何.*注册'
    ]
    if any(re.search(pattern, keyword_lower) for pattern in registration_patterns):
        return '1.注册相关'
    
    # 2. 登录使用 (Login & Usage)  
    login_patterns = [
        r'登录', r'login', r'用不了', r'打不开', r'无法访问', r'进不去', r'登陆',
        r'无法.*使用', r'不能.*用', r'访问.*不了', r'突然.*进不去'
    ]
    if any(re.search(pattern, keyword_lower) for pattern in login_patterns):
        return '2.登录使用'
    
    # 3. 下载安装 (Download & Install)
    download_patterns = [
        r'下载', r'download', r'安装', r'app', r'apk', r'安装包', r'客户端',
        r'ios.*安装', r'android', r'安卓', r'中文.*版'
    ]
    if any(re.search(pattern, keyword_lower) for pattern in download_patterns):
        return '3.下载安装'
    
    # 4. API服务 (API Services)
    api_patterns = [
        r'api', r'接口', r'调用', r'key', r'购买.*api', r'api.*购买',
        r'api.*key', r'openai.*api', r'gpt.*api', r'免费.*api'
    ]
    if any(re.search(pattern, keyword_lower) for pattern in api_patterns):
        return '4.API服务'
    
    # 5. Plus会员 (Plus Membership)
    plus_patterns = [
        r'plus', r'订阅', r'会员', r'购买', r'充值', r'代充', r'代.*充',
        r'plus.*购买', r'购买.*plus', r'信用卡', r'支付', r'虚拟.*信用卡'
    ]
    if any(re.search(pattern, keyword_lower) for pattern in plus_patterns):
        return '5.Plus会员'
    
    # 6. 技术问题 (Technical Issues)
    technical_patterns = [
        r'502', r'503', r'bad.*gateway', r'unable.*to.*load', r'something.*went.*wrong',
        r'验证.*真人', r'cloudflare.*验证', r'error', r'错误', r'验证.*循环',
        r'一直.*验证', r'转圈', r'响应.*时间.*过.*长', r'ssl.*错误', r'unusual.*activity'
    ]
    if any(re.search(pattern, keyword_lower) for pattern in technical_patterns):
        return '6.技术问题'
    
    # 7. 账号管理 (Account Management)
    account_patterns = [
        r'账号', r'共享', r'封号', r'被.*封', r'deactivated', r'账号.*共享',
        r'共享.*账号', r'账号.*购买', r'购买.*账号', r'被.*拒绝', r'被.*标记.*滥用'
    ]
    if any(re.search(pattern, keyword_lower) for pattern in account_patterns):
        return '7.账号管理'
    
    # 8. 模型功能 (Model Features)
    model_patterns = [
        r'gpt-?4', r'gpt-?4o', r'gpt-?3\.?5', r'turbo', r'免费', r'功能', r'区别',
        r'模型', r'版本', r'限制', r'使用.*次数', r'什么.*是', r'是.*什么',
        r'o1', r'插件', r'sora'
    ]
    if any(re.search(pattern, keyword_lower) for pattern in model_patterns):
        return '8.模型功能'
    
    # 默认分类
    return '9.其他'

def process_csv_files():
    """
    处理两个CSV文件，添加分类列并排序
    """
    # 文件路径
    file1_path = '/Users/lin/code/js/blog/doc/keyword/keyword1.csv'
    file2_path = '/Users/lin/code/js/blog/doc/keyword/keyword2.csv'
    
    print("开始处理CSV文件...")
    
    # 读取CSV文件
    try:
        df1 = pd.read_csv(file1_path, encoding='utf-8')
        print(f"成功读取 keyword1.csv，共 {len(df1)} 行数据")
    except Exception as e:
        print(f"读取 keyword1.csv 失败: {e}")
        return
    
    try:
        df2 = pd.read_csv(file2_path, encoding='utf-8')
        print(f"成功读取 keyword2.csv，共 {len(df2)} 行数据")
    except Exception as e:
        print(f"读取 keyword2.csv 失败: {e}")
        return
    
    # 为每个数据框添加分类列
    print("正在对关键词进行分类...")
    df1['关键词分类'] = df1['Keyword'].apply(classify_keyword)
    df2['关键词分类'] = df2['Keyword'].apply(classify_keyword)
    
    # 按分类排序
    df1_sorted = df1.sort_values(['关键词分类', 'Traffic'], ascending=[True, False])
    df2_sorted = df2.sort_values(['关键词分类', 'Traffic'], ascending=[True, False])
    
    # 统计各分类的数量
    print("\n=== keyword1.csv 分类统计 ===")
    category_counts1 = df1['关键词分类'].value_counts().sort_index()
    for category, count in category_counts1.items():
        print(f"{category}: {count} 个关键词")
    
    print("\n=== keyword2.csv 分类统计 ===")
    category_counts2 = df2['关键词分类'].value_counts().sort_index()
    for category, count in category_counts2.items():
        print(f"{category}: {count} 个关键词")
    
    # 保存处理后的文件
    output1_path = '/Users/lin/code/js/blog/doc/keyword/keyword1_classified.csv'
    output2_path = '/Users/lin/code/js/blog/doc/keyword/keyword2_classified.csv'
    
    try:
        df1_sorted.to_csv(output1_path, index=False, encoding='utf-8-sig')
        print(f"\n已保存分类后的文件: {output1_path}")
        
        df2_sorted.to_csv(output2_path, index=False, encoding='utf-8-sig')
        print(f"已保存分类后的文件: {output2_path}")
        
        # 合并两个文件
        combined_df = pd.concat([df1_sorted, df2_sorted], ignore_index=True)
        combined_df = combined_df.sort_values(['关键词分类', 'Traffic'], ascending=[True, False])
        
        combined_output_path = '/Users/lin/code/js/blog/doc/keyword/keywords_combined_classified.csv'
        combined_df.to_csv(combined_output_path, index=False, encoding='utf-8-sig')
        print(f"已保存合并分类文件: {combined_output_path}")
        
        print("\n=== 合并文件分类统计 ===")
        combined_counts = combined_df['关键词分类'].value_counts().sort_index()
        for category, count in combined_counts.items():
            print(f"{category}: {count} 个关键词")
        
        print(f"\n处理完成！总共处理了 {len(combined_df)} 个关键词")
        
    except Exception as e:
        print(f"保存文件失败: {e}")

if __name__ == "__main__":
    process_csv_files()