from huggingface_hub import scan_cache_dir


try:
    cache_info = scan_cache_dir()
    all_revisions = [revision.commit_hash for repo in cache_info.repos for revision in repo.revisions]

    delete_strategy = cache_info.delete_revisions(*all_revisions)
    print("Will free " + delete_strategy.expected_freed_size_str)

    delete_strategy.execute()
    print("Cache deletion done.")

except Exception as e:
    print(f"Error: {e}. No cache directory found, skipping cache deletion.")
