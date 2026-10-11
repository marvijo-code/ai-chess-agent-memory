# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0027-20261011-075651)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 33 | 268826 | 132096 | 49.1% | 49.0% |
| GPT-6.1 Sol | 62 | 2528967 | 2361088 | 93.4% | 93.5% |
| Sonnet 5.5 | 19 | 235661 | 212681 | 90.2% | 92.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7077 | 79054288 | 39942144 | 50.5% | 50.5% |
| GPT-6.1 Sol | 5606 | 162682702 | 151484288 | 93.1% | 93.6% |
| Sonnet 5.5 | 5846 | 128668225 | 122837879 | 95.5% | 96.1% |
