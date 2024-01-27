
# Chat Uygulaması

Bu basit chat uygulaması, bir istemci ve bir sunucu tarafından kullanılarak gerçek zamanlı iletişim sağlar. İstemci ve sunucu Python dilinde yazılmıştır ve basit bir çoklu kullanıcı chat odası oluşturur.

## İstemci Kullanımı

1. `ChatClient` sınıfını kullanarak istemciyi başlatın.
2. Kullanıcı adınızı girdikten sonra sunucuya bağlanın.
3. Mesajları göndermek ve almak için uygun yönergeleri izleyin.


```python
if __name__ == "__main__":
    HOST = '0.0.0.0'  # Sunucu IP adresi
    PORT = 44444
    USERNAME = input("Kullanıcı adınızı girin: ")

    client = ChatClient(HOST, PORT, USERNAME)
    client.connect_to_server()
```

## Sunucu Kullanımı

1. `ChatServer` sınıfını kullanarak sunucuyu başlatın.
2. Sunucu, belirtilen IP adresi ve port üzerinde dinlemeye başlar.
3. İstemciler bağlandıkça sunucu yeni bağlantıları kabul eder ve mesajları yayınlar.

```python
if __name__ == "__main__":
    HOST = '0.0.0.0'  # Sunucu IP adresi
    PORT = 44444

    server = ChatServer(HOST, PORT)
    server.start_server()
```

## Bağımlılıklar

- Python 3.x
- Kullanılan tüm kütüphaneler python dahili kütüphaneleridir

## Geliştirme

Proje üzerinde geliştirme yapmak istiyorsanız, bu adımları takip edebilirsiniz:

1. Kodu yerel bir bilgisayarınıza kopyalayın.
2. İlgili Python sürümünü yükleyin.
