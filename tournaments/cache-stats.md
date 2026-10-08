# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 326 | 3965564 | 1904640 | 48.0% | 48.0% |
| GPT-6.1 Sol | 160 | 3609330 | 3298688 | 91.4% | 91.9% |
| Sonnet 5.5 | 270 | 6710213 | 6454616 | 96.2% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 563 | 6301662 | 3181312 | 50.5% | 50.5% |
| GPT-6.1 Sol | 462 | 13163344 | 12202752 | 92.7% | 93.0% |
| Sonnet 5.5 | 539 | 12315893 | 11816421 | 95.9% | 96.4% |
