# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0018-20261010-074818)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 224 | 2416813 | 1095296 | 45.3% | 45.2% |
| GPT-6.1 Sol | 150 | 3718577 | 3421696 | 92.0% | 92.9% |
| Sonnet 5.5 | 173 | 3636844 | 3468803 | 95.4% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4726 | 51944249 | 24777472 | 47.7% | 47.6% |
| GPT-6.1 Sol | 3819 | 109083794 | 101196032 | 92.8% | 93.3% |
| Sonnet 5.5 | 4070 | 89407202 | 85369551 | 95.5% | 96.1% |
