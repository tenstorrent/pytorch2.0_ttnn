from huggingface_hub import scan_cache_dir


cache_info = scan_cache_dir()
all_revisions = []
for repo in cache_info.repos:
    all_revisions.extend(repo.revisions)

delete_strategy = cache_info.delete_revisions(*all_revisions)
print("Will free " + delete_strategy.expected_freed_size_str)

delete_strategy.execute()
print("Cache deletion done.")
