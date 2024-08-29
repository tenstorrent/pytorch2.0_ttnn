from huggingface_hub import scan_cache_dir

cache_dir = scan_cache_dir()
all_revisions = cache_dir.revisions

print(f"Found {len(all_revisions)} revisions.")

delete_strategy = cache_dir.delete_revisions(*all_revisions)
print("Will free " + delete_strategy.expected_freed_size_str)

delete_strategy.execute()
print("Cache deletion done.")
