LOAD CSV WITH HEADERS FROM 'file:///siga-empreendimentos-geracao_saida2.csv' AS row
CREATE (n:Usina:Hidreletrica {
    DatGeracaoConjuntoDados: row.DatGeracaoConjuntoDados,
    NomEmpreendimento: row.NomEmpreendimento,
    IdeNucleoCEG: row.IdeNucleoCEG,
    CodCEG: row.CodCEG,
    SigUFPrincipal: row.SigUFPrincipal,
    SigTipoGeracao: row.SigTipoGeracao,
    DscFaseUsina: row.DscFaseUsina,
    DscOrigemCombustivel: row.DscOrigemCombustivel,
    DscFonteCombustivel: row.DscFonteCombustivel,
    DscTipoOutorga: row.DscTipoOutorga,
    NomFonteCombustivel: row.NomFonteCombustivel,
    DatEntradaOperacao: row.DatEntradaOperacao,
    MdaPotenciaOutorgadaKw: row.MdaPotenciaOutorgadaKw,
    MdaPotenciaFiscalizadaKw: row.MdaPotenciaFiscalizadaKw,
    MdaGarantiaFisicaKw: row.MdaGarantiaFisicaKw,
    IdcGeracaoQualificada: row.IdcGeracaoQualificada,
    NumCoordNEmpreendimento: row.NumCoordNEmpreendimento,
    NumCoordEEmpreendimento: row.NumCoordEEmpreendimento,
    DatInicioVigencia: row.DatInicioVigencia,
    DatFimVigencia: row.DatFimVigencia,
    DscPropriRegimePariticipacao: row.DscPropriRegimePariticipacao,
    DscSubBacia: row.DscSubBacia,
    DscMuninicpios: row.DscMuninicpios
})
