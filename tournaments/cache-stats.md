# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0029-20261011-130205)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 57 | 637778 | 398336 | 62.5% | 62.6% |
| GPT-6.1 Sol | 27 | 540923 | 478592 | 88.5% | 91.0% |
| Sonnet 5.5 | 35 | 634726 | 597464 | 94.1% | 95.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7628 | 85438985 | 43741184 | 51.2% | 51.2% |
| GPT-6.1 Sol | 6103 | 178030891 | 165889792 | 93.2% | 93.6% |
| Sonnet 5.5 | 6261 | 137549272 | 131306534 | 95.5% | 96.1% |
