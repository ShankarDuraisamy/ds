#ifndef STATIC_ARRAY
#define STATIC_ARRAY

template <typename T>
class StaticArray
{
private:
    T data_;
    int len_
public:
    StaticArray(int capacity);
    ~StaticArray() { delete[] data_; }
    int len() const { return len_; }
    const T& operator[](int i) const { return data_[i]; } 
    T& operator[](int i) { return data_[i]; }
    Array& operator= (const Array&);
    void insert(T value, int location = 0);
    void remove(T value, int location = 0);
    
};

#endif