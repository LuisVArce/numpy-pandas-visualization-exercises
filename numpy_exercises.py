{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "725a2a51",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4fab8dda",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "40cb91c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 1\n",
    "negative_numbers = a < 0\n",
    "len(a[negative_numbers])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "db2ccde6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 2\n",
    "positive_numbers = a > 0\n",
    "len(a[positive_numbers])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7d825fe7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 3\n",
    "positive_even_numbers = (a > 0),\n",
    "(a % 2 == 0)\n",
    "len(a[positive_even_numbers])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f75374b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 4\n",
    "# If you were to add 3 to each data point, how many positive numbers would there be?\n",
    "positive_numbers = (a + 3) > 0\n",
    "len(a[positive_numbers])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6ab19048",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "64.99999999999999"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 5\n",
    "# If you squared each number, what would the new mean and standard deviation be?\n",
    "a.mean() ** 2\n",
    "a.std() ** 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0527afa6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0.,\n",
       "       -10.])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Exercise 6\n",
    "# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.\n",
    "\n",
    "a - a.mean()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "3e422152",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,\n",
       "       -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,\n",
       "        0.        , -1.24034735])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 7\n",
    "# # Z = x − μ / σ\n",
    "(a - a.mean()) / a.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8fb5fc8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercise 8\n",
    "## Setup 1\n",
    "a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c04dbf55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n"
     ]
    }
   ],
   "source": [
    "# Use python's built in functionality/operators to determine the following:\n",
    "# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list\n",
    "def sum_of_a(nums):\n",
    "    sum_list = 0\n",
    "    for num in nums:\n",
    "        sum_list = sum_list + num\n",
    "    return sum_list\n",
    "print(sum_of_a(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "78498bdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n"
     ]
    }
   ],
   "source": [
    "# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list\n",
    "def min_of_a(nums):\n",
    "    min_list = 0\n",
    "    for num in nums:\n",
    "        min_list = min_list + num\n",
    "    return min_list\n",
    "print(min_of_a(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f3ec46ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "f056ae19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<module 'matplotlib.pyplot' from '/opt/homebrew/anaconda3/lib/python3.9/site-packages/matplotlib/pyplot.py'>\n"
     ]
    }
   ],
   "source": [
    "print(plt)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b312176",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7671547",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
