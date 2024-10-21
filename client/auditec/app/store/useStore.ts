import { create } from "zustand";

// Defina a interface para o estado
interface Store {
  queryParam: string;
  setQueryParam: (param: string) => void;
}

// Crie a store usando a interface
export const useParamsStore = create<Store>((set) => ({
  queryParam: "",
  setQueryParam: (param: string) => set({ queryParam: param }),
}));

interface DataStore {
  dataStore: any[];
  setDataStore: (data: any) => void;
}

export const useDataStore = create<DataStore>((set) => ({
  dataStore: [],
  setDataStore: (data: any) => set({ dataStore: data }),
}));
