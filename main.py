from sprider.Zhihu import SearchZhihu

if __name__ == '__main__':
    keyword = '' # 你要搜索的关键词
    result = SearchZhihu(keyword=keyword).search()
    print(result)