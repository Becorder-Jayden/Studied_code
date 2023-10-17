### 2023.10.16
``` javascript
// selectedRow.license 값을 이용해 /license/get api 호출, 원하는 데이터 출력
const { list,getLicense,listLicense } = useLicense();  // useLicense에 정의 해둔 list, get,License, listLicense 가져오기 
const [license, setLicense ] = useState([]);  // fetchGetLicense에서 license값을 변경하기 위해 변수 정의

const fetchLicense = async (arg) => {
	try {
		await setLoading(true);
		await listLicense(queryString(arg), { meta: arg });  // listLicense 매서드를 통해 list 값 갱신
		await setLoading(false);
	} catch (e) {
		await setLoading(false);
	}
};

const fetchGetLicense = async (id) => {
	try {
		await setLoading(true);
		const reponse = await getLicense(id);  // license 값 불러오기 
		await setLicense(reponse.data);  // reponse에 저장한 data 값을 불러와 license 변수에 저장 
		await setLoading(false);
	} catch (e) {
		await setLoading(false);
	}
};

useEffect(() => {
	if (selectedRow && selectedRow.license) {  // license 값이 확보되었을 때
		fetchGetLicense(selectedRow.license);  // seletecRow.license (id)를 통해 license 값 변경
	}
}, [selectedRow]);

```