#!/usr/bin/env python3
import requests
import redis
from typing import Callable
from functools import wraps

# Initialize Redis client
r = redis.Redis()

def cache_result(method: Callable) -> Callable:
    """
    Decorator to cache the result of a function and set an expiration time.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to handle caching and counting.
        """
        # Define the cache key
        cache_key = f"cached:{url}"

        # Check if the result is already cached
        cached_result = r.get(cache_key)
        if cached_result:
            return cached_result.decode('utf-8')

        # Fetch the HTML content using the original method
        result = method(url)

        # Cache the result and set expiration to 10 seconds
        r.setex(cache_key, 10, result)

        return result
    
    return wrapper

def count_requests(method: Callable) -> Callable:
    """
    Decorator to count the number of times a URL is requested.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to handle counting.
        """
        # Define the count key
        count_key = f"count:{url}"

        # Increment the count for this URL
        r.incr(count_key)

        # Call the original method
        return method(url)
    
    return wrapper

@count_requests
@cache_result
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL.
    """
    response = requests.get(url)
    return response.text
