# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0015-20261010-001334)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 62 | 718623 | 301696 | 42.0% | 41.8% |
| GPT-6.1 Sol | 35 | 790669 | 707456 | 89.5% | 89.7% |
| Sonnet 5.5 | 46 | 1040842 | 991836 | 95.3% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3669 | 39854462 | 18421120 | 46.2% | 46.1% |
| GPT-6.1 Sol | 3165 | 92408460 | 85834624 | 92.9% | 93.3% |
| Sonnet 5.5 | 3340 | 74663800 | 71345618 | 95.6% | 96.1% |
